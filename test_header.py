import unittest
from header import Header

class HeaderTest(unittest.TestCase):

    def test_parse_header(self):
        f = open('test.a')
        data = f.read()
        header, data = Header.parse_header(data[8:])
        self.assertNotEqual(header, None)
        self.assertEqual(header.get_file_identifier(), "LICENSE")
        self.assertEqual(header.get_modification_time(), 1525176954)
        self.assertEqual(header.get_owner_id(), 502)
        self.assertEqual(header.get_group_id(), 20)
        self.assertEqual(header.get_file_mode(), "100644")
        self.assertEqual(header.get_file_size(), 1074)
        self.assertEqual(header.get_ending(), '`\n')
        self.assertEqual(len(data), 1186)
        f.close()

    def test_get_header_bytes(self):
        header = Header("LICENSE", 1525176954, 502, 20, "100644", 1074, '`\n')
        data = Header.get_header_bytes(header)
        f = open('test.a')
        expected_data = f.read()
        expected_data = expected_data[8:68]
        self.assertEqual(data, expected_data)
        f.close()

if __name__ == '__main__':
    unittest.main()
