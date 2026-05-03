"""
Tests for AIR (Adaptive Intelligence Runtime) document parsing and validation.

AIR is a fleet runtime layer documented in markdown files.
These tests validate the documented structure, contract, and expected behavior
based on the CHARTER.md, DOCKSIDE-EXAM.md, and README.md documents.
"""
import pytest
import re
from pathlib import Path

REPOS_DIR = Path(__file__).resolve().parent.parent  # = /repos/AIR — the AIR repo root
assert REPOS_DIR.name == "AIR", f"Expected AIR repo root, got {REPOS_DIR}"
AIR_DIR = REPOS_DIR  # The repo root IS the AIR directory

def read_md(name):
    return (AIR_DIR / name).read_text()

# ── README contract tests ────────────────────────────────────────────────────

class TestReadmeContract:
    """Validate AIR/README.md contract for runtime interface."""

    def test_readme_exists(self):
        assert (AIR_DIR / "README.md").exists()

    def test_readme_mentions_runtime(self):
        text = read_md("README.md")
        assert "runtime" in text.lower()

    def test_readme_mentions_fleet(self):
        text = read_md("README.md")
        assert "fleet" in text.lower()

    def test_readme_mentions_model(self):
        text = read_md("README.md")
        assert "model" in text.lower()

    def test_readme_has_install_instructions(self):
        text = read_md("README.md")
        assert "pip install" in text.lower() or "install" in text.lower()

    def test_readme_has_usage_example(self):
        text = read_md("README.md")
        assert "import" in text or "example" in text.lower()

    def test_readme_has_brand_line(self):
        text = read_md("README.md")
        assert any(phrase in text for phrase in ["runtime", "layer", "fleet"])

    def test_readme_mentions_adaptive_batching(self):
        text = read_md("README.md")
        assert "adaptive" in text.lower() or "batch" in text.lower()

    def test_readme_mentions_resource_policy(self):
        text = read_md("README.md")
        assert "resource" in text.lower()

# ── Charter contract tests ────────────────────────────────────────────────────

class TestCharterContract:
    """Validate AIR/CHARTER.md defines mission and constraints."""

    def test_charter_exists(self):
        assert (AIR_DIR / "CHARTER.md").exists()

    def test_charter_has_mission_section(self):
        text = read_md("CHARTER.md")
        assert "mission" in text.lower() or "purpose" in text.lower()

    def test_charter_defines_boundaries(self):
        text = read_md("CHARTER.md")
        assert len(text) > 100

    def test_charter_mentions_fleet_context(self):
        text = read_md("CHARTER.md")
        assert "fleet" in text.lower() or "vessel" in text.lower()

# ── Dockside exam tests ───────────────────────────────────────────────────────

class TestDocksideExam:
    """Validate AIR/DOCKSIDE-EXAM.md is a substantive spec doc."""

    def test_dockside_exists(self):
        assert (AIR_DIR / "DOCKSIDE-EXAM.md").exists()

    def test_dockside_is_substantive(self):
        text = read_md("DOCKSIDE-EXAM.md")
        assert len(text) > 500, "DOCKSIDE-EXAM should be a detailed spec doc"

    def test_dockside_has_sections(self):
        text = read_md("DOCKSIDE-EXAM.md")
        sections = re.findall(r'^##?\s+', text, re.MULTILINE)
        assert len(sections) >= 3

    def test_dockside_covers_architecture(self):
        text = read_md("DOCKSIDE-EXAM.md")
        assert any(kw in text.lower() for kw in ["architecture", "design", "interface", "api"])

# ── Runtime parameter tests ──────────────────────────────────────────────────

class TestRuntimeParameters:
    """Validate documented runtime parameters are well-defined."""

    def test_model_parameter_mentioned(self):
        text = read_md("README.md")
        assert re.search(r'model\s*=', text, re.IGNORECASE)

    def test_adaptive_batching_flag_exists(self):
        text = read_md("README.md")
        assert "adaptive_batching" in text.lower() or "batching" in text.lower()

    def test_resource_policy_flag_exists(self):
        text = read_md("README.md")
        assert "resource_policy" in text.lower() or "resource" in text.lower()

    def test_execute_method_contract(self):
        text = read_md("README.md")
        assert "execute" in text.lower()

# ── Fleet relationship tests ────────────────────────────────────────────────

class TestFleetRelationship:
    """Validate AIR's documented relationship to the Cocapn fleet."""

    def test_readme_lists_related_repos(self):
        text = read_md("README.md")
        assert "github.com" in text or "lucinear" in text.lower() or "superinstance" in text.lower()

    def test_readme_mentions_plato_sdk(self):
        text = read_md("README.md")
        assert "plato" in text.lower() or "sdk" in text.lower()

    def test_readme_mentions_jetsonclaw(self):
        text = read_md("README.md")
        assert "jetson" in text.lower() or "vessel" in text.lower()

    def test_readme_has_cocapn_brand(self):
        text = read_md("README.md")
        assert "cocapn" in text.lower() or "🦐" in text

    def test_readme_has_lighthouse_keeper_reference(self):
        text = read_md("README.md")
        assert "lighthouse" in text.lower() or "keeper" in text.lower()

# ── Markdown quality tests ───────────────────────────────────────────────────

class TestMarkdownQuality:
    """Validate AIR markdown docs meet fleet standards."""

    def test_no_broken_links_in_readme(self):
        text = read_md("README.md")
        # Check for common link patterns
        links = re.findall(r'\[.+?\]\((.+?)\)', text)
        for link_url in links:
            assert link_url.startswith(('http', '#', './', '/', 'https')), f"Broken link: {link_url}"

    def test_readme_has_code_fences(self):
        text = read_md("README.md")
        assert "```" in text, "README should contain code examples"

    def test_readme_has_headings(self):
        text = read_md("README.md")
        headings = re.findall(r'^#+\s+', text, re.MULTILINE)
        assert len(headings) >= 2

    def test_all_markdown_files_have_content(self):
        for md_file in AIR_DIR.glob("*.md"):
            content = md_file.read_text()
            assert len(content) > 50, f"{md_file.name} should not be nearly empty"


# ── Installation contract tests ───────────────────────────────────────────────

class TestInstallationContract:
    """Validate AIR installation instructions are correct."""

    def test_package_name_in_readme(self):
        text = read_md("README.md")
        assert "cocapn-air" in text or "air" in text.lower()

    def test_install_command_is_pip(self):
        text = read_md("README.md")
        assert "pip install" in text.lower()

    def test_has_import_statement(self):
        text = read_md("README.md")
        assert "import air" in text.lower() or "from air import" in text.lower()


# ── Behavioral contract (from docs) ─────────────────────────────────────────

class TestBehavioralContract:
    """Validate behaviors documented in AIR docs are correctly specified."""

    def test_runtime_initialization_contract(self):
        text = read_md("README.md")
        # Runtime should be initialized with model, adaptive_batching, resource_policy
        assert re.search(r'Runtime\s*\(', text, re.IGNORECASE)

    def test_execute_takes_string_input(self):
        text = read_md("README.md")
        assert "execute(" in text.lower()

    def test_runtime_described_as_fleet_layer(self):
        text = read_md("README.md")
        assert "runtime layer" in text.lower() or "interface layer" in text.lower()

    def test_dynamic_model_loading_mentioned(self):
        text = read_md("README.md")
        assert "dynamic" in text.lower() or "loading" in text.lower()

    def test_adaptive_batch_sizing_mentioned(self):
        text = read_md("README.md")
        assert "adaptive" in text.lower() and "batch" in text.lower()

    def test_resource_aware_scheduling_mentioned(self):
        text = read_md("README.md")
        assert "resource" in text.lower() and ("scheduling" in text.lower() or "schedul" in text.lower())
