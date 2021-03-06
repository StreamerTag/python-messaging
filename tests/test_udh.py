from unittest import TestCase

from messaging.sms.udh import UserDataHeader
from messaging.utils import hex_to_int_array


class TestUserDataHeader(TestCase):

    def test_user_data_header(self):
        data = hex_to_int_array("08049f8e020105040b8423f0")
        udh = UserDataHeader.from_bytes(data)

        self.assertEqual(udh.concat.seq, 1)
        self.assertEqual(udh.concat.cnt, 2)
        self.assertEqual(udh.concat.ref, 40846)
        self.assertEqual(udh.ports.dest_port, 2948)
        self.assertEqual(udh.ports.orig_port, 9200)

        data = hex_to_int_array("0003190201")
        udh = UserDataHeader.from_bytes(data)

        self.assertEqual(udh.concat.seq, 1)
        self.assertEqual(udh.concat.cnt, 2)
        self.assertEqual(udh.concat.ref, 25)
