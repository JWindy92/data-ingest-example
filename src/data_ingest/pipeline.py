from openbao_client import OpenBaoClient


def run(bao: OpenBaoClient) -> dict[str, int | str]:
    credentials = bao.get_secret("data_ingest")

    api_key = credentials["api_key"]

    # Placeholder for actual ingestion work.
    #
    # data = fetch_data(api_key)
    # transformed = transform(data)
    # store(transformed)

    return {
        "status": "ok",
        "message": "Pipeline executed successfully",
        "api_key_length": len(api_key),
    }