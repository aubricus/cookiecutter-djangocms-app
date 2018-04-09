app_slug = "{{ cookiecutter.app_slug }}"


if hasattr(app_slug, "isidentifier"):
    assert_fail_msg = "Project slug should be valid Python identifier!"
    assert app_slug.isidentifier(), assert_fail_msg
