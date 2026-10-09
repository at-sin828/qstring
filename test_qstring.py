import unittest

from qstring import build_query, first_value, has_key, key_names, parse_query, value_count, without_key


class QstringTest(unittest.TestCase):
    def test_repeated_keys(self) -> None:
        got = parse_query("?tag=a&tag=b&q=")
        self.assertEqual(got, {"tag": ["a", "b"], "q": [""]})
        self.assertEqual(parse_query(build_query(got)), got)
        self.assertEqual(first_value(got, "tag"), "a")
        self.assertEqual(first_value(got, "missing", "no"), "no")
        self.assertEqual(without_key(got, "tag"), {"q": [""]})
        self.assertEqual(value_count(got, "tag"), 2)
        self.assertEqual(value_count(got, "missing"), 0)
        self.assertTrue(has_key(got, "tag"))
        self.assertFalse(has_key(got, "missing"))
        self.assertEqual(key_names(got), ["tag", "q"])
        self.assertEqual(got["tag"], ["a", "b"])


if __name__ == "__main__":
    unittest.main()
