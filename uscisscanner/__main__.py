__author__ = 'Stanley Li'

from uscisscanner.util.argparser import run_parser
from uscisscanner.util.ExcelWriter import ExcelWriter

import time
import copy
import sys

import mechanize
from bs4 import BeautifulSoup


APPROVED_STATUSES = ['Case Was Approved']
DECLINED_STATUSES = []
PROCESSING_STATUSES = []


def scan_receipts(startid, length, interval):
    print("Start Scanning USCIS receipt number %s to %s. Estimated time: %s" %
          (startid, startid + length - 1, (time.strftime("%H Hours %M Mins %S Secs", time.gmtime(length * interval)))))
    caseid = startid
    webtexts = {}
    for number in xrange(length):
        br = mechanize.Browser()
        br.open("https://egov.uscis.gov/casestatus/mycasestatus.do")
        br.select_form(name='caseStatusForm')
        br.form['appReceiptNum'] = str(caseid)  # 'LIN1590452504'
        response = br.submit()
        soup = BeautifulSoup(response)

        ''' Now only one h1 flag should be found '''
        assert len(soup.find_all('h1')) <= 1, "USCIS has changed website layout!"
        text = ""
        if len(soup.find_all('h1')) != 0:
            for link in soup.find_all('h1'):
                text = link.parent.get_text()

        webtexts[copy.copy(caseid)] = text
        print "Finished checking case: %s, progress %d/%d" % (caseid, number + 1, length)
        if number != length - 1:
            caseid += 1
            time.sleep(interval)
    return webtexts


def main():
    args = run_parser()
    web_texts = scan_receipts(args.startId, args.scanNumber, args.scanInterval)
    datafile = ExcelWriter(args.outputFile)
    datafile.write_to_file(web_texts)
    datafile.close()


if __name__ == '__main__':
    sys.exit(main())
