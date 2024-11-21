import flet as ft
from flet_route import Params, Basket
from utils.style import *



class DashboardPage():
    def view(self, page: ft.Page, params: Params, basket: Basket):
        page.title = "Панель управления"
        page.window.width = defaultWidthWindow
        page.window.height = defaultWidthWindow
        page.window.min_width = 900
        page.window.min_height = 400
        page.fonts = {"cuprum": "fonts/Cuprum.ttf"}


        def input_form(label):
            return ft.TextField(label=f'{label}',
                                bgcolor=secondaryBgColor,
                                border=ft.InputBorder.NONE,
                                filled=True,
                                color=secondaryFontColor
                                )
        #style_menu
        style_menu = ft.ButtonStyle(color={ft.ControlState.HOVERED: ft.colors.WHITE,
                                           ft.ControlState.DEFAULT: menuFontColor},
                                    overlay_color=hoverBgcolor,
                                    shadow_color=hoverBgcolor
                                    )

        #sidebar
        logo = ft.Container(
            padding=ft.padding.symmetric(17, 13),
            content=ft.Row(
                controls=[
                    ft.Image(src='images/logo.jpg', width=45, height=32, fit=ft.ImageFit.FILL),
                    ft.Text('Tdashboard', expand=True, color=defaultFontColor, font_family='cuprum', size=16)
                ],
                alignment=ft.MainAxisAlignment.START,
                vertical_alignment=ft.CrossAxisAlignment.CENTER
            )
        )

        #menu
        sidebar_menu = ft.Container(
            padding=ft.padding.symmetric(0, 13),
            content=ft.Column(
                controls=[
                    ft.Text('МЕНЮ', color=menuFontColor, size=12, font_family='cuprum'),
                    ft.TextButton('Главная', icon='space_dashboard_rounded', style=style_menu),
                    ft.TextButton('Постинг', icon='post_add', style=style_menu),
                    ft.TextButton('Тестовая кнопка', icon='verified_user', style=style_menu),
                ]
            )
        )

        token_input = ft.Container(
            content=input_form('Введите токен бота'),
            border_radius=15
        )
        channel_input = ft.Container(
            content=input_form('Введите токен бота'),
            border_radius=15
        )

        save_button = ft.ElevatedButton('Сохранить данные',
                                        bgcolor=hoverBgcolor,
                                        color=defaultFontColor,
                                        icon='settings')


        #start_header
        header = ft.Container(content=ft.Row(controls=[
            ft.Text('Панель управления', color=defaultFontColor, size=20, font_family='cupurum'),
            ft.Row(
                controls=[
                    ft.CircleAvatar(
                        foreground_image_src='images/avatar.jpg',
                        content=ft.Text('A')),
                    ft.IconButton(
                        icon=ft.icons.NOTIFICATIONS_ROUNDED,
                        icon_size=20,
                        hover_color=hoverBgcolor,
                        icon_color=defaultFontColor,
                    )
                ], alignment=ft.MainAxisAlignment.END,

            )
        ], alignment=ft.MainAxisAlignment.SPACE_BETWEEN))


        return ft.View(
            "/dashboard",
            controls=[
                # ft.Container(content=input_form('введите токен бота'))
                ft.Row(
                    expand=True,
                    controls=[
                        #left
                        ft.Container(
                            expand=1,
                            content=ft.Column(
                                controls=[
                                    logo,
                                    sidebar_menu
                                ]
                            ),
                            bgcolor=secondaryBgColor,
                        ),
                        #body center
                        ft.Container(
                            expand=4,
                            padding=ft.padding.symmetric(15, 10),
                            content=ft.Column([header, token_input, channel_input, save_button])
                        )

                    ]
                )
            ],
            bgcolor=defaultBgColor,
            padding=0
        )