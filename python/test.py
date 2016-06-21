import unittest
import linkedlist as ll

class linkedlisttests(unittest.TestCase):
    def test_if_list_is_empty(self):
        newlist = ll.LinkedList()

        self.assertTrue(newlist.empty())
        newlist.insert(1)
        self.assertFalse(newlist.empty())

    def test_insert_no_position(self):
        newlist = ll.LinkedList()

        newlist.insert(1)
        self.assertNotEqual(newlist.find(1), -1)
        newlist.insert(2)
        self.assertNotEqual(newlist.find(1), -1)
        self.assertNotEqual(newlist.find(2), -1)

if __name__ == '__main__':
    unittest.main()
