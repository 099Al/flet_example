import flet as ft
from flet_route import Params, Basket
from utils.style import *



class DashboardPage():
    def view(self, page: ft.Page, params: Params, basket: Basket):
        page.title = "Dashboard"
        page.window.width = defaultWidthWindow
        page.window.height = defaultWidthWindow
        page.window.min_width = 800
        page.window.min_height = 400
        page.fonts = {"cuprum": "fonts/Cuprum.ttf"}

        return ft.View(
            "/dashboard",
            controls=[
                ft.Text('Панель управления')
            ]
        )