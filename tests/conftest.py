"""Pytest configuration for the sdx package tests."""

from __future__ import annotations

import os
import warnings

from pathlib import Path

import pytest

from dotenv import dotenv_values, load_dotenv


@pytest.fixture
def env() -> dict[str, str | None]:
    """Return a fixture for the environment variables from .env file."""
    dotenv_path = Path(__file__).parents[1] / '.envs' / '.env'
    if not dotenv_path.exists():
        warnings.warn(
            f"'.env' file not found at {dotenv_path}. Some "
            'tests requiring environment variables might fail or be skipped.'
        )
        return {}

    load_dotenv(dotenv_path=dotenv_path)
    return dotenv_values(dotenv_path)


@pytest.fixture
def test_data_dir() -> Path:
    """Fixture providing the path to the test data directory."""
    return Path(__file__).parent / 'data'


@pytest.fixture
def reports_pdf_dir(test_data_dir: Path) -> Path:
    """Fixture for the directory containing PDF report files."""
    pdf_dir = test_data_dir / 'reports' / 'pdf_reports'
    if not pdf_dir.exists():
        pdf_dir.mkdir(parents=True, exist_ok=True)
    return pdf_dir


@pytest.fixture
def reports_image_dir(test_data_dir: Path) -> Path:
    """Fixture for the directory containing image report files."""
    image_dir = test_data_dir / 'reports' / 'image_reports'
    if not image_dir.exists():
        image_dir.mkdir(parents=True, exist_ok=True)
    return image_dir


@pytest.fixture
def api_key_openai(env: dict[str, str | None]) -> str:
    """Fixture providing the OpenAI API key from environment variables."""
    api_key = os.getenv('OPENAI_API_KEY')

    if not api_key:
        raise EnvironmentError(
            'Please set the OPENAI_API_KEY environment variable in your .env '
            'file or system environment for testing.'
        )

    return api_key
