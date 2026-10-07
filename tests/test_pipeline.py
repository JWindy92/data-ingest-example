from unittest.mock import Mock

from data_ingest.pipeline import run


def test_pipeline():
    bao = Mock()

    bao.get_secret.return_value = {
        "api_key": "test-api-key",
    }

    result = run(bao)

    bao.get_secret.assert_called_once_with("data_ingest")

    assert result == {
        "status": "ok",
        "message": "Pipeline executed successfully",
        "api_key_length": 12,
    }
