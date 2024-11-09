from django.shortcuts import render
from django.views import View


class HomePage(View):

    template_name = "home/index.html"

    def get(self, request):

        menu_data = [
        {
            'id': 1,
            'name': 'Menu 1',
            'subMenu': [
                {'name': 'Submenu 1', 'desc': 'Description 1',
                    'icon': 'path/to/icon1.svg'},
                {'name': 'Submenu 2', 'desc': 'Description 2',
                    'icon': 'path/to/icon2.svg'},
            ],
            'gridCols': 3,
        },
        {
            'id': 2,
            'name': 'Menu 2',
            'subMenu': [
                {'name': 'Submenu A', 'desc': 'Description A',
                    'icon': 'path/to/iconA.svg'},
                {'name': 'Submenu B', 'desc': 'Description B',
                    'icon': 'path/to/iconB.svg'},
            ],
            'gridCols': 2,
        },
        ]
        context = {
            'menu' : menu_data
        }
        return render(request=request, template_name=self.template_name,context=context)
