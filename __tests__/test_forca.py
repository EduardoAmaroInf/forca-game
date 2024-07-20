import pytest
import os

# Importar as funções que queremos testar
from forca import ler_palavra_secreta, desenhar_forca, exibir_progresso

def test_ler_palavra_secreta(tmp_path):
    # Criar um arquivo temporário
    palavra_teste = "python"
    arquivo_teste = tmp_path / "word.txt"
    arquivo_teste.write_text(palavra_teste)
    
    # Testar a função ler_palavra_secreta
    assert ler_palavra_secreta(arquivo_teste) == palavra_teste

def test_desenhar_forca():
    # Testar as diferentes etapas do desenho da forca
    for i in range(7):
        desenho = desenhar_forca(i)
        assert isinstance(desenho, str)
        assert '+' in desenho
        assert '=' in desenho

def test_exibir_progresso():
    palavra_secreta = "python"
    letras_corretas = {'p', 'y'}
    
    # Testar o progresso com algumas letras corretas
    progresso = exibir_progresso(palavra_secreta, letras_corretas)
    assert progresso == "py____"
    
    letras_corretas = {'p', 'y', 't', 'h', 'o', 'n'}
    progresso = exibir_progresso(palavra_secreta, letras_corretas)
    assert progresso == "python"
    
    letras_corretas = set()
    progresso = exibir_progresso(palavra_secreta, letras_corretas)
    assert progresso == "______"

# Para rodar os testes, use o comando `pytest` no terminal na pasta onde o arquivo de testes está localizado.
