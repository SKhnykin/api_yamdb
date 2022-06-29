import django_filters as filters
from reviews.models import Title


class TitlesFilters(filters.FilterSet):
    name = filters.CharFilter(field_name='name', lookup_expr='contains')
    year = filters.NumberFilter(field_name='year')
    category = filters.CharFilter(field_name='category__slug')
    genre = filters.CharFilter(field_name='genre__slug')

    class Meta:
        model = Title
        fields = '__all__'
