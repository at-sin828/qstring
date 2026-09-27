import unittest

from qstring import build_query, parse_query


class QstringTest(unittest.TestCase):
    def test_repeated_keys(self) -> None:
        got = parse_query("?tag=a&tag=b&q=")
        self.assertEqual(got, {"tag": ["a", "b"], "q": [""]})
        self.assertEqual(parse_query(build_query(got)), got)


if __name__ == "__main__":
    unittest.main()
