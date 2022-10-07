from flask import Blueprint, request, render_template, redirect, url_for

# from assets.unit_classes import unit_classes
from lesson_c4.assets.units import Player, Enemy
from lesson_c4.app.setup import heroes, equipment, unit_classes


# Define Blueprint
start_bp = Blueprint('Start', __name__)


@start_bp.route('/')
def start():
    """Display start page"""
    return render_template('index.html')


@start_bp.route('/choose-hero/', methods=['GET', 'POST'])
def choose_hero():
    """Display player unit configuration form"""

    if request.method == 'GET':
        result = {
            "header": 'Выбор героя для игрока',
            "classes": unit_classes,
            "weapons": equipment.get_weapon_names(),
            "armors": equipment.get_armor_names()
        }

        return render_template('hero_choosing.html', result=result)

    if request.method == 'POST':
        # Get form data
        user_name = request.form.get('name')
        unit_class = unit_classes[request.form.get('unit_class')]
        weapon = equipment.get_weapon(request.form.get('weapon'))
        armor = equipment.get_armor(request.form.get('armor'))

        # Create hero
        player_unit = Player(name=user_name, unit_class=unit_class, weapon=weapon, armor=armor)
        heroes['player'] = player_unit

        return redirect(url_for('Start.choose_enemy'))


@start_bp.route('/choose-enemy/', methods=['GET', 'POST'])
def choose_enemy():
    """Display enemy unit configuration form"""

    if request.method == 'GET':
        result = {
            "header": 'Выбор героя для врага',
            "classes": unit_classes,
            "weapons": equipment.get_weapon_names(),
            "armors": equipment.get_armor_names()
        }

        return render_template('hero_choosing.html', result=result)

    if request.method == 'POST':
        # Get form data
        user_name = request.form.get('name')
        unit_class = unit_classes[request.form.get('unit_class')]
        weapon = equipment.get_weapon(request.form.get('weapon'))
        armor = equipment.get_armor(request.form.get('armor'))

        # Create unit
        enemy_unit = Enemy(name=user_name, unit_class=unit_class, weapon=weapon, armor=armor)
        heroes['enemy'] = enemy_unit

        return redirect(url_for('Fight.fight', _external=True))
