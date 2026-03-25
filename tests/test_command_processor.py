from siri_assistant.core.command_processor import CommandProcessor


class StubLLM:
    def ask(self, query: str) -> str:
        return f"echo:{query}"


def test_opens_known_site() -> None:
    processor = CommandProcessor(StubLLM())
    result = processor.process("open youtube")

    assert result.action == "open_url"
    assert result.url == "https://youtube.com"


def test_time_command() -> None:
    processor = CommandProcessor(StubLLM())
    result = processor.process("what is the time")

    assert result.action == "speak"
    assert "The time is" in result.text


def test_fallback_to_llm() -> None:
    processor = CommandProcessor(StubLLM())
    result = processor.process("tell me a joke")

    assert result.text == "echo:tell me a joke"
