import wmill

from openbao_client import OpenBaoClient

from data_ingest.pipeline import run


def main():
    token = wmill.get_variable("f/infrastructure/openbao_token")

    bao = OpenBaoClient(
        address="http://openbao:8200",
        token=token,
    )

    return run(bao)
