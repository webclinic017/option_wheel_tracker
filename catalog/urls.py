from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('tickers/', views.StockTickerListView.as_view(), name='tickers'),
    path('tickers/<int:pk>', views.StockTickerDetailView.as_view(), name='ticker-detail'),
    path('tickers/create/', views.StockTickerCreate.as_view(), name='ticker-create'),
    path('tickers/<int:pk>/update/', views.StockTickerUpdate.as_view(), name='ticker-update'),
    path('tickers/<int:pk>/delete/', views.StockTickerDelete.as_view(), name='ticker-delete'),
    path('wheels/', views.OptionWheelListView.as_view(), name='wheels'),
    path('wheels/<int:pk>', views.OptionWheelDetailView.as_view(), name='wheel-detail'),
    path('wheels/<int:wheel_id>/purchase/<int:pk>', views.OptionPurchaseDetailView.as_view(), name='purchase-detail-view'),
    path('wheels/<int:wheel_id>/purchase/create/', views.OptionPurchaseCreate.as_view(), name='purchase-create'),
    path('wheels/<int:wheel_id>/purchase/<int:pk>/update/', views.OptionPurchaseUpdate.as_view(), name='purchase-update'),
    path('wheels/<int:wheel_id>/purchase/<int:pk>/delete/', views.OptionPurchaseDelete.as_view(), name='purchase-delete'),
    path('wheels/create/', views.create_wheel, name='wheel-create'),
    path('wheels/<int:pk>/delete/', views.OptionWheelDelete.as_view(), name='wheel-delete'),

]