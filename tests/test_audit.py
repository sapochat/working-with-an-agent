import importlib.util, unittest
from pathlib import Path
p = Path(__file__).parents[1] / "scripts/audit_agreement.py"
spec = importlib.util.spec_from_file_location("audit_agreement", p); mod = importlib.util.module_from_spec(spec); spec.loader.exec_module(mod)

class AuditTests(unittest.TestCase):
    def test_template_passes(self):
        text = (Path(__file__).parents[1] / "templates/working-agreement.md").read_text()
        self.assertEqual(mod.audit(text), [])
    def test_secret_is_flagged(self):
        text = "quality communication grounding completion approval memory\n" + "API_" + "KEY=abc123"
        self.assertTrue(any("credential" in x for x in mod.audit(text)))
    def test_private_ipv4_findings_include_complete_address(self):
        text = "quality communication grounding completion approval memory\n"
        findings = mod.audit(text + "10.1.2.3 172.16.4.5 192.168.6.7")
        self.assertTrue(any("10.1.2.3" in x for x in findings))
        self.assertTrue(any("172.16.4.5" in x for x in findings))
        self.assertTrue(any("192.168.6.7" in x for x in findings))

if __name__ == "__main__": unittest.main()
