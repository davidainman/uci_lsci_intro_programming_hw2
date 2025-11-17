from io import StringIO

def test_char_counter(monkeypatch, capsys):
    from char_counter import char_counter

    monkeypatch.setattr(
        'sys.stdin', 
        StringIO("Well hello there!@\n")
    )
    char_counter()
    captured = capsys.readouterr()
    assert "'W': 1" in captured.out
    assert "'e': 4" in captured.out
    assert "'l': 4" in captured.out
    assert "' ': 2" in captured.out
    assert "'h': 2" in captured.out
    assert "'o': 1" in captured.out
    assert "'t': 1" in captured.out
    assert "'r': 1" in captured.out
    assert "'!': 1" in captured.out
    assert "'@': 1" in captured.out

    monkeypatch.setattr('sys.stdin', StringIO("\n"))
    char_counter()
    captured = capsys.readouterr()
    assert "{}" in captured.out

def test_duplicate_remover(capsys):
    from duplicate_remover import duplicate_remover
    duplicate_remover([5, 6, 0, 1, 6, 5, 0, 1, 9, 4])
    captured = capsys.readouterr()
    assert "[5, 6, 0, 1, 9, 4]" in captured.out
    duplicate_remover([3, 2, 3, 3, 2, 1, 1, 4, 2, 3])
    captured = capsys.readouterr()
    assert "[3, 2, 1, 4]" in captured.out

def test_even_square_sum(monkeypatch, capsys):
    from even_square_sum import even_square_sum
    even_square_sum([1, 62, 3, 57, 26, 8, 101, 200, 43, 20, 11])
    captured = capsys.readouterr()
    assert "44984" == captured.out.strip()
    even_square_sum([4, 16, 19, 5, 104, 23, 99])
    captured = capsys.readouterr()
    assert "11088" == captured.out.strip()

def test_grocery_calculator(monkeypatch, capsys):
    from grocery_calculator import grocery_calculator
    inputs = iter(['bread', 'milk', 'eggs', 'butter', 'eggs', ''])
    monkeypatch.setattr('builtins.input', lambda msg: next(inputs))
    grocery_calculator()
    captured = capsys.readouterr()
    assert '$21' in captured.out

    monkeypatch.setattr('builtins.input', lambda msg: '')
    grocery_calculator()
    captured = capsys.readouterr()
    assert '$0' in captured.out

def test_temperature_calculator(monkeypatch, capsys):
    from temperature_calculator import temperature_calculator

    inputs = iter(['40', '28', '64', 'quit'])
    monkeypatch.setattr('builtins.input', lambda msg: next(inputs))
    temperature_calculator()
    captured = capsys.readouterr()
    assert '44.0' in captured.out
