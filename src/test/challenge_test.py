from challenge import challenge

facts = {
    ('gabriel', 'endereço', 'av rio branco, 109', True),
    ('joão', 'endereço', 'rua alice, 10', True),
    ('joão', 'endereço', 'rua bob, 88', True),
    ('joão', 'telefone', '234-5678', True),
    ('joão', 'telefone', '91234-5555', True),
    ('joão', 'telefone', '234-5678', False),
    ('gabriel', 'telefone', '98888-1111', True),
    ('gabriel', 'telefone', '56789-1010', True),
}

schema = {
    ('endereço', 'cardinality', 'one'),
    ('telefone', 'cardinality', 'many')
}


def test_challenge_should_have_correct_vector():
    processed = challenge(facts, schema)
    expected_via = {
        ('gabriel', 'endereço', 'av rio branco, 109', True),
        ('joão', 'endereço', 'rua bob, 88', True),
        ('joão', 'telefone', '91234-5555', True),
        ('joão', 'telefone', '234-5678', True),
        ('gabriel', 'telefone', '98888-1111', True),
        ('gabriel', 'telefone', '56789-1010', True)
    }
    assert processed == expected_via
