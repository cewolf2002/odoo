# -*- coding: utf-8 -*-
# To get this module for Odoo(OpenERP) v7.0, please refer:
# https://github.com/Odoo-India/odoo-india
# 
# Ported to Odoo 8.0 by youring@gmail.com 
#
###############################################################################
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as published
# by the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
###############################################################################
{
    'name': 'Custom Filter Tabs',
    'version': '8.1',
    'category': 'Tools',
    'summary': 'Custom Filter Tabs',
    'description': """
Converts custom filters into tabs 
将自定义搜索结果以标签形式显示
===========================================
A very convenient feature of OpenERP that can convert your custom filters into tabs to make searching easy and enhances your GUI experience.

将保存的搜索（过滤）结果直接以标签发方式显示在视图上方，类似于多标签页（IE中叫选项卡）浏览器的操作方式，方便省事~

    """,
    'author': 'youring',
    'website': 'http://git.oschina.net/youring',
    'depends': [
        'base', 
        'web',
    ],
    'data': [
        'views/web_filter_tabs.xml',
    ],
    
    'qweb': [
        'static/src/xml/web_filter_tabs.xml',
    ],
    'installable': True,
    'auto_install': False,
}

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
