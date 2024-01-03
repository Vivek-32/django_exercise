from django.shortcuts import HttpResponse, render
from .models import Country, City, State

def insert_data(request):
    country = Country(name='USA', country_code='US', curr_symbol='$', phone_code='+1')
    country.save()

    state = State(name='California', state_code='CA', gst_code='GSTCA', country=country)
    state.save()

    city = City(name='Los Angeles', city_code='LA', phone_code='+1', population=4000000, avg_age=35.5, num_of_adult_males=2000000, num_of_adult_females=2000000, state=state)
    city.save()

    return HttpResponse("Data inserted successfully.")


def bulk_insert_data(request):
    countries = [Country(name='India', country_code='IN', curr_symbol='₹', phone_code='+91'),
                 Country(name='France', country_code='FR', curr_symbol='EUR', phone_code='+44')]
    Country.objects.bulk_create(countries)

    states = [State(name='Telangana', state_code='TS', gst_code='GSTTS', country=Country.objects.get(country_code='IN')),
              State(name='Delhi', state_code='DL', gst_code='GSTDL', country=Country.objects.get(country_code='IN'))]
    State.objects.bulk_create(states)

    cities = [City(name='Hyderabad', city_code='HYD', phone_code='+91', population=4000000, avg_age=35.5, num_of_adult_males=2000000, num_of_adult_females=2000000, state=State.objects.get(state_code='TS')),
              City(name='New Delhi', city_code='ND', phone_code='+91', population=2000000, avg_age=30.0, num_of_adult_males=1000000, num_of_adult_females=1000000, state=State.objects.get(state_code='DL'))]
    City.objects.bulk_create(cities)

    return HttpResponse("Bulk data inserted successfully.")

def bulk_update_data(request):
    Country.objects.filter(country_code="IN").update(curr_symbol='#')
    
    State.objects.filter(state_code="CA").update(gst_code="NEWGSTCA")
    
    City.objects.filter(city_code="HYD").update(avg_age=37.0)
    
    return HttpResponse("Bulk data update successfully")

def fetch_all(request):
    countries = Country.objects.all()
    states = State.objects.all()
    cities = City.objects.all()
    return render(request,'templates/fetch_all.html', {'countries': countries, 'states': states, 'cities': cities})

def cities_in_state(request):
    cities = City.objects.filter(state__state_code='TS')
    return render(request,'templates/cities_in_state.html', {'cities': cities})
    
def states_in_country(request):
    states = State.objects.filter(country__country_code="IN")
    print(states)
    
def cities_in_country(request):
    cities = City.objects.filter(state__country__country_code="IN")
    print(cities)
    
def get_population(request):
    min_population = City.objects.filter(state__country__country_code="IN").order_by('population').first()
    max_population = City.objects.filter(state__country__country_code="IN").order_by('population').last()
    print('Max Population: {}, Min Population: {}'.format(max_population, min_population))