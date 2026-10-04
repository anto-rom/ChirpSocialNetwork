import pytest

from red_social.publicacion import Retweet, Tweet


@pytest.mark.parametrize(
    "texto",
    [
        "",
        " ",
        "x" * 281,
    ],
)
def test_texto_invalido_lanza_error(ana, texto):
    with pytest.raises(ValueError):
        Tweet(ana, texto)


@pytest.mark.parametrize(
    "texto, esperado",
    [
        ("Hola #Python", ["#python"]),
        ("#Python #PYTHON", ["#python"]),
        ("Hola #python, #pytest!", ["#python", "#pytest"]),
        ("Esto # no cuenta", []),
    ],
)
def test_extraer_hashtags(texto, esperado):
    assert Tweet.extraer_hashtags(texto) == esperado


def test_retweet_comparte_el_texto_del_original(tweet, luis):
    retweet = Retweet(luis, tweet)

    assert retweet.original is tweet
    assert retweet.texto == tweet.texto
    assert retweet.hashtags == tweet.hashtags
    assert retweet.autor is luis
