from red_social.publicacion import Tweet
from red_social.red import RedSocial


def test_timeline_solo_muestra_seguidos_y_mas_reciente_primero(red):
    ana = red["@ana"]
    luis = red["@luis"]
    marta = red["@marta"]

    tweet_ana = red.publicar(Tweet(ana, "Tweet de Ana"))
    tweet_marta = red.publicar(Tweet(marta, "Tweet de Marta"))
    tweet_ana_2 = red.publicar(Tweet(ana, "Otro tweet de Ana"))

    timeline_luis = red.timeline(luis)

    assert timeline_luis == [tweet_ana_2, tweet_ana]
    assert tweet_marta not in timeline_luis
    assert red.timeline(ana) == []


def test_desde_json_carga_usuarios_y_seguimientos(mocker):
    contenido = """
    {
        "usuarios": [
            {"nombre": "Ana", "alias": "@ana"},
            {"nombre": "Luis", "alias": "@luis"}
        ],
        "seguimientos": [
            ["@luis", "@ana"]
        ]
    }
    """

    mock_archivo = mocker.mock_open(read_data=contenido)
    mocker.patch("builtins.open", mock_archivo)

    red = RedSocial.desde_json("usuarios.json")

    mock_archivo.assert_called_once_with("usuarios.json", encoding="utf-8")
    assert len(red) == 2
    assert red["@luis"].sigue_a(red["@ana"])
