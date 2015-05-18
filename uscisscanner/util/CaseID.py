__author__ = 'Stanley Li'


class CaseID(object):
    def __init__(self, service_center, receipt_number):
        assert type(service_center) is str, "Service center name must be String"
        self._serviceCenter = service_center
        if type(receipt_number) in [str, int, long]:
            try:
                self._receiptNumber = long(receipt_number)
            except ValueError:
                assert 0, "receiptNumber must be all digits!"
        else:
            assert 0, "Receipt number must be all digits"

    def __iadd__(self,  other):
        self._receiptNumber += other
        return self

    def __radd__(self,  other):
        return self.__class__(self._serviceCenter, self._receiptNumber + other)

    def __add__(self,  other):
        return self.__class__(self._serviceCenter, self._receiptNumber + other)

    def __sub__(self,  other):
        return self.__class__(self._serviceCenter, self._receiptNumber - other)

    def __str__(self):
        return self._serviceCenter + str(self._receiptNumber)

    def __gt__(self, other):
        assert isinstance(other, self.__class__), "Not implemented __gt__!"
        return self._receiptNumber > other._receiptNumber

    def __hash__(self):
        """ Only use Receipt number to hash is enough """
        return hash(self._receiptNumber)

    def __eq__(self, other):
        assert isinstance(other, self.__class__), "Not implemented __eq__!"
        return (self._serviceCenter, self._receiptNumber) == (other._serviceCenter, other._receiptNumber)