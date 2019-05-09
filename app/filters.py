from django_filters import filters
from django_filters import FilterSet
from .models import Item


class MyOrderingFilter(filters.OrderingFilter):
    descending_fmt = '%s （降順）'


class ItemFilter(FilterSet):

    station_name= filters.CharFilter(label='駅名', lookup_expr='contains')
    furigana = filters.CharFilter(label='ふりがな', lookup_expr='contains')
    organization1 = filters.ChoiceFilter(choices=Item.OGName_CHICES)
    organization2 = filters.ChoiceFilter(choices=Item.OGName_CHICES)
    organization3 = filters.ChoiceFilter(choices=Item.OGName_CHICES)
    organization4 = filters.ChoiceFilter(choices=Item.OGName_CHICES)
    organization5 = filters.ChoiceFilter(choices=Item.OGName_CHICES)
    organization6 = filters.ChoiceFilter(choices=Item.OGName_CHICES)
    memo = filters.CharFilter(label='備考', lookup_expr='contains')

    order_by = MyOrderingFilter(
        # tuple-mapping retains order
        fields=(
            ('station_name', 'station_name'),
            ('furigana', 'furigana'),
        ),
        field_labels={
            'station_name': '駅名',
            'furigana': 'ふりがな',
        },
        label='並び順'
    )

    class Meta:

        model = Item
        fields = ('station_name', 'furigana', 'organization1', 'organization2', 'organization3', 'organization4', 'organization5', 'organization6', 'memo',)
