# Testing_AniLiberty

## Описание

Проект содержит автоматизированные тесты для проверки функциональности:
- Веб-приложения AniLiberty (UI-автотесты с использованием Selenium и Page Object)
- REST API AniLibria (API-автотесты с использованием библиотеки requests)

## Требования (в проекте используются следующие технологии)

- Python 3.8+
- pytest
- selenium
- requests
- allure-pytest
- Установленная в системе утилита Allure Report

## Форматирование кода

- Код форматируется в соответствии со стандартами PEP8
- Для проверки используется линтер flake8:
  flake8 .

## Структура проекта

- `pages/` — пакет с классами страниц (Page Object Model) для UI-тестов
- `tests/` — пакет, содержащий тестовые сценарии (`test_ui_*.py` и `test_api_*.py`)
- `requirements.txt` — список зависимостей проекта
- `README.md` — документация к проекту

## Установка

1. Клонировать репозиторий
2. Установить зависимости:
  pip install -r requirements.txt

## Запуск тестов

pytest

## Запуск тестов с формированием Allure отчета

pytest --alluredir=allure-results

## Запуск просмотра сформированного отчета Allure

allure serve allure-results

## Выход (Завершить выполнение)

Нажмите Ctrl+C для выхода.
