import importlib.util,pathlib,unittest
p=pathlib.Path(__file__).resolve().parents[1]/"exposure_monitor.py"
s=importlib.util.spec_from_file_location("tool",p);m=importlib.util.module_from_spec(s);s.loader.exec_module(m)
class Tests(unittest.TestCase):
 def test_empty_text(self): self.assertEqual(m.analyze_text(""),[])
 def test_returns_list(self): self.assertIsInstance(m.analyze_text("sample input"),list)
if __name__=="__main__":unittest.main()
