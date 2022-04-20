from os import walk
import unittest
import pep8


class TestPep8(unittest.TestCase):
    def test_pep8(self):
        style = pep8.StyleGuide(quiet=True)
        style.options.ignore += ("E402",)
        style.options.max_line_length = 112
        errors = 0
        python_files = []
        exclude = ("python")
        for output in walk("."):
            for _file in output[2]:
                if output[0].lstrip('./').startswith(exclude):
                    continue
                if (_file.endswith(".py")):
                    python_files.append(output[0] + "/" + _file)
        for _file in python_files:
            result = style.check_files([_file])
            if (result.get_file_results() != 0):
                print(result.filename + ':')
                for _issue in result.get_statistics():
                    print(_issue)
        self.assertEqual(result.total_errors,
                         0,
                         'PEP8 validation issues: %d'
                         % result.total_errors)


if __name__ == "__main__":
    unittest.main()
