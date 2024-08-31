from playground.models import Country,MovieTypes

def get_valid_countries():
    countries = Country.objects.all()
    return [country.Country for country in countries]

def is_valid_country(country_name):
    valid_countries = get_valid_countries()
    return country_name in valid_countries


def get_valid_movietypes():
    MT = MovieTypes.objects.all()
    return [TypesOfMovies.TypesOfMovies for TypesOfMovies in MT]

def is_valid_movietype(MovieTypeName):
    valid_MT = get_valid_movietypes()
    return MovieTypeName in valid_MT
    