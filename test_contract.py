import unittest
from robots_route_contract import trace, check

class ContractTests(unittest.TestCase):
    def test_longest(self):
        r=trace("User-agent: *\nDisallow: /private\nAllow: /private/public", "DemoBot", "/private/public/a")
        self.assertTrue(r["allowed"]);self.assertEqual(r["winning_rule"]["line"],3)
    def test_tie_allow(self):
        self.assertTrue(trace("User-agent: *\nDisallow: /a\nAllow: /a","Bot","/a")["allowed"])
    def test_exact_over_wildcard(self):
        r=trace("User-agent: *\nDisallow: /\nUser-agent: Bot\nAllow: /", "Bot", "/a")
        self.assertTrue(r["allowed"]);self.assertEqual(r["group"],"exact")
    def test_merge_exact(self):
        r=trace("User-agent: Bot\nDisallow: /a\nUser-agent: Bot\nDisallow: /b","Bot","/b")
        self.assertFalse(r["allowed"])
    def test_end_anchor(self):
        t="User-agent: *\nDisallow: /*.pdf$"
        self.assertFalse(trace(t,"Bot","/x.pdf")["allowed"])
        self.assertTrue(trace(t,"Bot","/x.pdf?q=1")["allowed"])
    def test_encoded_reserved_literal(self):
        t="User-agent: *\nDisallow: /literal%2A"
        self.assertFalse(trace(t,"Bot","/literal%2a")["allowed"])
        self.assertTrue(trace(t,"Bot","/literalabc")["allowed"])
    def test_unreserved_decode(self):
        self.assertFalse(trace("User-agent: *\nDisallow: /abc","Bot","/%61bc")["allowed"])
    def test_unicode(self):
        self.assertFalse(trace("User-agent: *\nDisallow: /café","Bot","/caf%C3%A9")["allowed"])
    def test_empty_disallow(self):
        self.assertTrue(trace("User-agent: *\nDisallow:","Bot","/a")["allowed"])
    def test_malformed_case(self):
        with self.assertRaises(ValueError):check("",[{"agent":"Bot","path":"/","allowed":"yes"}])
    def test_bad_escape(self):
        with self.assertRaises(ValueError):trace("","Bot","/%QQ")
    def test_raw_star_literal(self):
        self.assertFalse(trace("User-agent: *\nDisallow: /literal%2A", "Bot", "/literal*")["allowed"])
    def test_raw_dollar_literal(self):
        self.assertFalse(trace("User-agent: *\nDisallow: /literal%24", "Bot", "/literal$")["allowed"])
    def test_robots_implicit(self):
        self.assertTrue(trace("User-agent: *\nDisallow: /", "Bot", "/robots.txt")["allowed"])
    def test_contract_mismatch(self):
        self.assertFalse(check("User-agent: *\nDisallow: /a",[{"agent":"Bot","path":"/a","allowed":True}])["ok"])

if __name__=="__main__":unittest.main()
