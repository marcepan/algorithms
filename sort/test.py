from QuickSort import Sort
import unittest

class TestSortingMethods(unittest.TestCase): 
      
    def setUp(self): 
        pass
  
    # def test_one_element(self): 
    #     unsorted_list = [5]
    #     self.assertListEqual(Sort(unsorted_list), unsorted_list)

    # def test_two_elements(self): 
    #     unsorted_list = [5,1]
    #     self.assertListEqual(Sort(unsorted_list), [1,5])

    # def test_three_elements(self): 
    #     unsorted_list = [5,1,4]
    #     self.assertListEqual(Sort(unsorted_list), [1,4,5])

    # def test_four_elements(self): 
    #     unsorted_list = [5,1,4,2]
    #     self.assertListEqual(Sort(unsorted_list), [1,2,4,5])

    # def test_negative_elements(self): 
    #     unsorted_list = [5,1,-4,2,4]
    #     self.assertListEqual(Sort(unsorted_list), [-4,1,2,4,5])

    # def test_no_elements(self): 
    #     unsorted_list = []
    #     self.assertListEqual(Sort(unsorted_list), unsorted_list)
    #     test
    
    def test_smallest_element_at_the_end(self): 
        unsorted_list = [5,1,2,4,0]
        self.assertListEqual(Sort(unsorted_list), [0,1,2,4,5])
    
    # def test_smallest_element_at_the_beginning(self): 
    #     unsorted_list = [0,5,1,2,4,0]
    #     self.assertListEqual(Sort(unsorted_list), [0,0,1,2,4,5])
  
if __name__ == '__main__': 
    unittest.main() 