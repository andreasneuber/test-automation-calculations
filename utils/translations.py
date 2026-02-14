# translations.py
"""
Multilingual translation module for English, German, French, and Luxembourgish support
"""

TRANSLATIONS = {
    'en': {
        'main': {
            'app_title': 'Test Automation Calculations',
            'sidebar_title': 'Navigation',
            'nav_label': 'Go to',
            'nav_home': 'HOME',
            'nav_q1': '1) How many work hours can be saved by automating the test suite?',
            'nav_q2': '2) How many test runs are needed to counter-balance the initial time investment for automating a test suite?',
            'nav_q3': '3) Can the team \'afford\' the maintenance of [n] more automated tests?',
            'language_label': 'Language'
        },
        'home': {
            'instructions': 'Intended usage: Follow the questions under Navigation one by one to avoid financial losses and frustrations.'
        },
        'question1': {
            'title': 'How many work hours can be saved by automating the test suite?',
            'input_manual': 'Manual Test Run Time of Test Suite (in hours):',
            'input_automated': 'Automated Test Run Time of Test Suite (in minutes):',
            'result_message': 'Each automated test run will save you about {time} hours.',
            'chart_title': 'Time Comparison: Manual vs Automated Test Suite',
            'chart_yaxis': 'Time (hours)',
            'chart_type': 'Type',
            'label_manual': 'Manual',
            'label_automated': 'Automated',
            'label_saved': 'Time Saved'
        },
        'question2': {
            'title': 'How many test runs are needed to counter-balance the initial time investment for automating a test suite?',
            'input_investment': 'Initial investment for automation (in hours)',
            'input_savings': 'Time savings per run (in hours)',
            'result_message': 'Number of test runs needed to counter-balance the initial investment: {runs}',
            'chart_title': 'Reaching Break-even Point for Automated Test Suite',
            'chart_xaxis': 'Number of Test Runs',
            'chart_yaxis': 'Cumulative Time Savings (hours)',
            'chart_annotation': 'Initial Investment',
            'chart_trace': 'Cumulative Time Savings',
            'hover_runs': 'Number of Runs',
            'hover_savings': 'Time Savings'
        },
        'question3': {
            'title': 'Can the team "afford" the maintenance of [n] more automated tests?',
            'input_th': 'Monthly hours available for maintenance tasks (TH):',
            'input_mt': 'Monthly hours currently used to maintain existing automated tests (MT):',
            'input_n': 'Total count of all current automated tests (N):',
            'input_a': 'Count of new automated tests to be added next month (A):',
            'warning_message': 'Adding more tests will lead to decay of the automation test suite.',
            'success_message': 'You can afford to add and maintain {count} more automated tests next month.',
            'chart_xaxis': 'Months',
            'chart_yaxis': 'Potential to add more tests (P)'
        },
        'months': ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
    },
    'de': {
        'main': {
            'app_title': 'Testautomatisierungs-Kalkulationen',
            'sidebar_title': 'Navigation',
            'nav_label': 'Gehe zu',
            'nav_home': 'START',
            'nav_q1': '1) Wie viele Arbeitsstunden können durch die Automatisierung der Testsuite eingespart werden?',
            'nav_q2': '2) Wie viele Testläufe sind erforderlich, um die anfängliche Zeitinvestition für die Automatisierung einer Testsuite auszugleichen?',
            'nav_q3': '3) Kann sich das Team die Wartung von [n] weiteren automatisierten Tests „leisten"?',
            'language_label': 'Sprache'
        },
        'home': {
            'instructions': 'Verwendungszweck: Folgen Sie den Fragen unter Navigation nacheinander, um finanzielle Verluste und Frustrationen zu vermeiden.'
        },
        'question1': {
            'title': 'Wie viele Arbeitsstunden können durch die Automatisierung der Testsuite eingespart werden?',
            'input_manual': 'Manuelle Testlaufzeit der Testsuite (in Stunden):',
            'input_automated': 'Automatisierte Testlaufzeit der Testsuite (in Minuten):',
            'result_message': 'Jeder automatisierte Testlauf spart Ihnen etwa {time} Stunden.',
            'chart_title': 'Zeitvergleich: Manuelle vs. automatisierte Testsuite',
            'chart_yaxis': 'Zeit (Stunden)',
            'chart_type': 'Typ',
            'label_manual': 'Manuell',
            'label_automated': 'Automatisiert',
            'label_saved': 'Zeitersparnis'
        },
        'question2': {
            'title': 'Wie viele Testläufe sind erforderlich, um die anfängliche Zeitinvestition für die Automatisierung einer Testsuite auszugleichen?',
            'input_investment': 'Anfangsinvestition für Automatisierung (in Stunden)',
            'input_savings': 'Zeitersparnis pro Lauf (in Stunden)',
            'result_message': 'Anzahl der Testläufe, die erforderlich sind, um die anfängliche Investition auszugleichen: {runs}',
            'chart_title': 'Erreichen des Break-Even-Punkts für automatisierte Testsuite',
            'chart_xaxis': 'Anzahl der Testläufe',
            'chart_yaxis': 'Kumulative Zeitersparnis (Stunden)',
            'chart_annotation': 'Anfangsinvestition',
            'chart_trace': 'Kumulative Zeitersparnis',
            'hover_runs': 'Anzahl der Läufe',
            'hover_savings': 'Zeitersparnis'
        },
        'question3': {
            'title': 'Kann sich das Team die Wartung von [n] weiteren automatisierten Tests „leisten"?',
            'input_th': 'Monatlich verfügbare Stunden für Wartungsaufgaben (TH):',
            'input_mt': 'Monatlich verwendete Stunden für die Wartung bestehender automatisierter Tests (MT):',
            'input_n': 'Gesamtzahl aller aktuellen automatisierten Tests (N):',
            'input_a': 'Anzahl neuer automatisierter Tests, die im nächsten Monat hinzugefügt werden sollen (A):',
            'warning_message': 'Das Hinzufügen weiterer Tests führt zum Verfall der automatisierten Testsuite.',
            'success_message': 'Sie können sich leisten, {count} weitere automatisierte Tests im nächsten Monat hinzuzufügen und zu warten.',
            'chart_xaxis': 'Monate',
            'chart_yaxis': 'Potenzial für weitere Tests (P)'
        },
        'months': ['Jan', 'Feb', 'Mär', 'Apr', 'Mai', 'Jun', 'Jul', 'Aug', 'Sep', 'Okt', 'Nov', 'Dez']
    },
    'fr': {
        'main': {
            'app_title': 'Calculs d\'automatisation de tests',
            'sidebar_title': 'Navigation',
            'nav_label': 'Aller à',
            'nav_home': 'ACCUEIL',
            'nav_q1': '1) Combien d\'heures de travail peuvent être économisées en automatisant la suite de tests ?',
            'nav_q2': '2) Combien de cycles de tests sont nécessaires pour compenser l\'investissement initial en temps pour l\'automatisation d\'une suite de tests ?',
            'nav_q3': '3) L\'équipe peut-elle « se permettre » la maintenance de [n] tests automatisés supplémentaires ?',
            'language_label': 'Langue'
        },
        'home': {
            'instructions': 'Usage prévu : Suivez les questions sous Navigation une par une pour éviter les pertes financières et les frustrations.'
        },
        'question1': {
            'title': 'Combien d\'heures de travail peuvent être économisées en automatisant la suite de tests ?',
            'input_manual': 'Durée d\'exécution manuelle de la suite de tests (en heures) :',
            'input_automated': 'Durée d\'exécution automatisée de la suite de tests (en minutes) :',
            'result_message': 'Chaque exécution de test automatisée vous fera économiser environ {time} heures.',
            'chart_title': 'Comparaison de temps : Suite de tests manuelle vs automatisée',
            'chart_yaxis': 'Temps (heures)',
            'chart_type': 'Type',
            'label_manual': 'Manuel',
            'label_automated': 'Automatisé',
            'label_saved': 'Temps économisé'
        },
        'question2': {
            'title': 'Combien de cycles de tests sont nécessaires pour compenser l\'investissement initial en temps pour l\'automatisation d\'une suite de tests ?',
            'input_investment': 'Investissement initial pour l\'automatisation (en heures)',
            'input_savings': 'Économie de temps par exécution (en heures)',
            'result_message': 'Nombre de cycles de tests nécessaires pour compenser l\'investissement initial : {runs}',
            'chart_title': 'Atteindre le seuil de rentabilité pour la suite de tests automatisée',
            'chart_xaxis': 'Nombre de cycles de tests',
            'chart_yaxis': 'Économies de temps cumulatives (heures)',
            'chart_annotation': 'Investissement initial',
            'chart_trace': 'Économies de temps cumulatives',
            'hover_runs': 'Nombre de cycles',
            'hover_savings': 'Économie de temps'
        },
        'question3': {
            'title': 'L\'équipe peut-elle « se permettre » la maintenance de [n] tests automatisés supplémentaires ?',
            'input_th': 'Heures mensuelles disponibles pour les tâches de maintenance (TH) :',
            'input_mt': 'Heures mensuelles actuellement utilisées pour maintenir les tests automatisés existants (MT) :',
            'input_n': 'Nombre total de tous les tests automatisés actuels (N) :',
            'input_a': 'Nombre de nouveaux tests automatisés à ajouter le mois prochain (A) :',
            'warning_message': 'L\'ajout de tests supplémentaires entraînera la dégradation de la suite de tests automatisée.',
            'success_message': 'Vous pouvez vous permettre d\'ajouter et de maintenir {count} tests automatisés supplémentaires le mois prochain.',
            'chart_xaxis': 'Mois',
            'chart_yaxis': 'Potentiel pour ajouter plus de tests (P)'
        },
        'months': ['jan.', 'fév.', 'mars', 'avr.', 'mai', 'juin', 'juil.', 'août', 'sept.', 'oct.', 'nov.', 'déc.']
    },
    'lb': {
        'main': {
            'app_title': 'Testautomatiséierungs-Berechnungen',
            'sidebar_title': 'Navigatioun',
            'nav_label': 'Gitt zu',
            'nav_home': 'HEEEM',
            'nav_q1': '1) Wéivill Aarbechtsstonnen kënne gespuert ginn duerch d\'Automatiséierung vun der Testsuite?',
            'nav_q2': '2) Wéivill Testleefer si néideg fir déi initial Zäitinvestitioun fir d\'Automatiséierung vun enger Testsuite auszegläichen?',
            'nav_q3': '3) Kann d\'Team sech d\'Maintenance vun [n] méi automatiséierte Tester "leeschten"?',
            'language_label': 'Sprooch'
        },
        'home': {
            'instructions': 'Virgesinnten Gebrauch:Follt d\'Froen ënner Navigatioun eent no deem aneren fir finanziell Verloschter a Frustratiounen ze vermeiden.'
        },
        'question1': {
            'title': 'Wéivill Aarbechtsstonnen kënne gespuert ginn duerch d\'Automatiséierung vun der Testsuite?',
            'input_manual': 'Manuell Testlafzäit vun der Testsuite (a Stonnen):',
            'input_automated': 'Automatiséiert Testlafzäit vun der Testsuite (a Minutten):',
            'result_message': 'All automatiséierten Testlaf spuert Iech ongeféier {time} Stonnen.',
            'chart_title': 'Zäitverglach: Manuell vs automatiséiert Testsuite',
            'chart_yaxis': 'Zäit (Stonnen)',
            'chart_type': 'Typ',
            'label_manual': 'Manuell',
            'label_automated': 'Automatiséiert',
            'label_saved': 'Zäiterspuernis'
        },
        'question2': {
            'title': 'Wéivill Testleefer si néideg fir déi initial Zäitinvestitioun fir d\'Automatiséierung vun enger Testsuite auszegläichen?',
            'input_investment': 'Initial Investitioun fir Automatiséierung (a Stonnen)',
            'input_savings': 'Zäiterspuernis pro Laf (a Stonnen)',
            'result_message': 'Unzuel vun Testleefer déi néideg si fir déi initial Investitioun auszegläichen: {runs}',
            'chart_title': 'Erreeche vum Break-Even-Punkt fir automatiséiert Testsuite',
            'chart_xaxis': 'Unzuel vun Testleefer',
            'chart_yaxis': 'Kumulativ Zäiterspuernis (Stonnen)',
            'chart_annotation': 'Initial Investitioun',
            'chart_trace': 'Kumulativ Zäiterspuernis',
            'hover_runs': 'Unzuel vun Leefer',
            'hover_savings': 'Zäiterspuernis'
        },
        'question3': {
            'title': 'Kann d\'Team sech d\'Maintenance vun [n] méi automatiséierte Tester "leeschten"?',
            'input_th': 'Monatlech verfügbar Stonnen fir Maintenance-Aufgaben (TH):',
            'input_mt': 'Monatlech benotzt Stonnen fir d\'Maintenance vun existéierende automatiséierte Tester (MT):',
            'input_n': 'Gesamtzuel vun allen aktuellen automatiséierte Tester (N):',
            'input_a': 'Unzuel vun neien automatiséierte Tester déi nächste Mount derbäigesat ginn (A):',
            'warning_message': 'Derbäisetze vu méi Tester féiert zum Verfall vun der automatiséierter Testsuite.',
            'success_message': 'Dir kënnt Iech leeschten {count} méi automatiséiert Tester am nächste Mount derbäizesetzen a ze erhalen.',
            'chart_xaxis': 'Méint',
            'chart_yaxis': 'Potenzial fir méi Tester (P)'
        },
        'months': ['Jan.', 'Feb.', 'Mäe.', 'Abr.', 'Mee', 'Juni', 'Juli', 'Aug.', 'Sept.', 'Okt.', 'Nov.', 'Dez.']
    }
}


def get_text(language, section, key):
    """
    Retrieve translated text for a given language, section, and key.
    
    Args:
        language (str): Language code ('en', 'de', 'fr', or 'lb')
        section (str): Section name (e.g., 'main', 'home', 'question1')
        key (str): Specific text key
        
    Returns:
        str: Translated text, or key name if not found
    """
    try:
        return TRANSLATIONS[language][section][key]
    except KeyError:
        return f"[Missing: {section}.{key}]"


def format_number(value, decimals, language):
    """
    Format a number according to language conventions.
    
    English: 1.5 (period as decimal separator)
    German/French/Luxembourgish: 1,5 (comma as decimal separator)
    
    Args:
        value (float): Number to format
        decimals (int): Number of decimal places
        language (str): Language code ('en', 'de', 'fr', or 'lb')
        
    Returns:
        str: Formatted number string
    """
    formatted = f"{value:.{decimals}f}"
    
    if language in ['de', 'fr', 'lb']:
        # Replace period with comma for German, French, and Luxembourgish
        formatted = formatted.replace('.', ',')
    
    return formatted


def get_months(language):
    """
    Get list of month abbreviations for the specified language.
    
    Args:
        language (str): Language code ('en', 'de', 'fr', or 'lb')
        
    Returns:
        list: List of 12 month abbreviations
    """
    return TRANSLATIONS.get(language, {}).get('months', TRANSLATIONS['en']['months'])
