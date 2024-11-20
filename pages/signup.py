import flet as ft
from flet_route import Params, Basket


class SignupPage:
    def view(self, page: ft.Page, params: Params, basket: Basket):
        page.title = 'Страница регистрации'

        return ft.View(
              '/signup',
              controls=[
                  ft.Text('Регистрация'),
                  ft.ElevatedButton('Страница регистрации', on_click=lambda e: page.go('/'))
              ]
        )