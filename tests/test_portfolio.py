import pathlib, sys, unittest
ROOT=pathlib.Path(__file__).resolve().parents[1]
sys.path.extend([str(ROOT/'python'),str(ROOT/'algorithms')])
from text_utils import normalize_whitespace, word_count, is_palindrome
from validators import is_valid_email, is_indian_pin_code, is_strong_password
from statistics_utils import describe
from searching import linear_search, binary_search
from sorting import merge_sort, quick_sort
from structures import Stack, Queue
class PortfolioTests(unittest.TestCase):
 def test_text(self):
  self.assertEqual(normalize_whitespace(' hi   there '),'hi there')
  self.assertEqual(word_count('red blue green'),3)
  self.assertTrue(is_palindrome('A man, a plan, a canal: Panama'))
 def test_validators(self):
  self.assertTrue(is_valid_email('x@example.com'))
  self.assertTrue(is_indian_pin_code('831001'))
  self.assertTrue(is_strong_password('Strong#123'))
 def test_stats(self): self.assertEqual(describe([1,2,3])['mean'],2)
 def test_search(self):
  self.assertEqual(linear_search([2,4,6],4),1)
  self.assertEqual(binary_search([2,4,6],6),2)
 def test_sort(self):
  self.assertEqual(merge_sort([3,1,2]),[1,2,3])
  self.assertEqual(quick_sort([3,1,2]),[1,2,3])
 def test_structures(self):
  s=Stack(); s.push('x'); self.assertEqual(s.pop(),'x')
  q=Queue(); q.enqueue('a'); q.enqueue('b'); self.assertEqual(q.dequeue(),'a')
if __name__=='__main__': unittest.main()
