from django.urls import path
from . import views
urlpatterns = [
    path('', views.home, name='about'),
    path('about/', views.about_us, name='about'),
    path('carrers/', views.careers, name='contact'),
    path('product/', views.product, name='product'),
    path('product/thermosolver/', views.thermosolver, name='thermosolver'),
    path('product/stressmaster/',views.stressmaster, name='stressmaster'),

    path('product/mech-ai/', views.mechai, name='mechai'),

path('product/fluid_flow_ai/', views.fluid_flow, name='fluid_flow'),

     path('product/design_master/',views.design_master, name='design_master'),

     path('product/manufactaring_twin/', views.manufactring_twin, name='manufactaring_twin'),

     path('product/robopilot_ai/', views.robopilot_ai, name='robopilot_ai'),
    path('product/mat_si/',views.mat_si, name='mat_si'),
]