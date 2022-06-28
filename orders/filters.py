import django_filters as filter
from django import forms



class OrderFilter(filter.FilterSet):
    CHOICES_RATING_DATE = (
        ('big_price', 'По высокой цене'),
        ('small_price', 'По низкой цене'),
        ('num', 'по id'),
    )

    ordering_by_rating_date = filter.ChoiceFilter(label='', choices=CHOICES_RATING_DATE,
                                                  method='filter_ordering_by_rating_date')

    def filter_ordering_by_rating_date(self, queryset, name, value):
        if value == 'big_price':
            sort = '-dol_price'
        elif value == 'small_price':
            sort = 'dol_price'
        elif value == 'num':
            sort = 'id'
        else:
            sort = '-id'
        return queryset.order_by(sort)
