import pytest


class TestSsh:
    @pytest.mark.complete("ssh -Fsp", cwd="ssh")
    def test_1(self, completion):
        assert completion == "-Fspaced  conf"

    @pytest.mark.complete("ssh -F config ls", cwd="ssh")
    def test_2(self, completion):
        """Should complete both commands and hostname."""
        assert all(x in completion for x in "ls ls_known_host".split())

    @pytest.mark.complete("ssh bash", cwd="ssh")
    def test_3(self, completion):
        """
        First arg should not complete with commands.

        Assumes there's no "bash" known host.
        """
        assert "bash" not in completion
