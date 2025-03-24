CREATE DATABASE empresa_pia;

-- Criação da tabela 'users'
CREATE TABLE IF NOT EXISTS users (
    id SERIAL PRIMARY KEY,
    email VARCHAR NOT NULL UNIQUE,
    hashed_password VARCHAR NOT NULL,
    name VARCHAR NOT NULL,
    phone VARCHAR NOT NULL,
    document VARCHAR NOT NULL,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT now()
);

-- Criação da tabela 'atividade_economica'
CREATE TABLE IF NOT EXISTS atividade_economica (
    id SERIAL PRIMARY KEY,
    codigo_cnae VARCHAR UNIQUE NOT NULL,
    descricao VARCHAR UNIQUE NOT NULL
);

-- Criação da tabela 'componente_transformacao'
CREATE TABLE IF NOT EXISTS componente_transformacao (
    id SERIAL PRIMARY KEY,
    nome VARCHAR UNIQUE NOT NULL
);

-- Criação da tabela 'periodo'
CREATE TABLE IF NOT EXISTS periodo (
    id SERIAL PRIMARY KEY,
    ano INTEGER UNIQUE NOT NULL
);

-- Criação da tabela 'dados_transformacao'
CREATE TABLE IF NOT EXISTS dados_transformacao (
    id SERIAL PRIMARY KEY,
    atividade_economica_id INTEGER NOT NULL REFERENCES atividade_economica(id) ON DELETE CASCADE,
    componente_id INTEGER NOT NULL REFERENCES componente_transformacao(id) ON DELETE CASCADE,
    periodo_id INTEGER NOT NULL REFERENCES periodo(id) ON DELETE CASCADE,
    valor DECIMAL(18, 2)
);

-- Índice composto para a tabela 'dados_transformacao'
CREATE INDEX IF NOT EXISTS ix_dados_transformacao_atividade_componente_periodo
    ON dados_transformacao(atividade_economica_id, componente_id, periodo_id);

-- Criação da tabela 'token_blacklist'
CREATE TABLE IF NOT EXISTS token_blacklist (
    token VARCHAR(255) PRIMARY KEY NOT NULL,
    created TIMESTAMP WITH TIME ZONE DEFAULT now() NOT NULL
);

INSERT INTO users (id, email, hashed_password, name, phone, document, created_at) VALUES
(1, 'admin@empresa.com', '$2b$12$abcdef1234567890abcdef1234567890abcdef1234567890abcdef12', 'Administrador', '85999999999', '07.264.385/0001-43', NOW()) ON CONFLICT (email) DO NOTHING;;

-- Inserção de 5 atividades econômicas
INSERT INTO atividade_economica (codigo_cnae, descricao) VALUES
    ('01.11-3', 'Cultivo de cereais'),
    ('02.20-9', 'Silvicultura'),
    ('10.11-2', 'Fabricação de produtos alimentícios'),
    ('23.30-4', 'Fabricação de artefatos de concreto'),
    ('47.81-4', 'Comércio varejista de artigos do vestuário')
ON CONFLICT (codigo_cnae) DO NOTHING;

-- Inserção de 5 componentes de transformação
INSERT INTO componente_transformacao (nome) VALUES
    ('Energia elétrica'),
    ('Mão de obra'),
    ('Matéria-prima'),
    ('Tecnologia'),
    ('Transporte')
ON CONFLICT (nome) DO NOTHING;

-- Inserção de 5 períodos (anos)
INSERT INTO periodo (ano) VALUES
    (2020),
    (2021),
    (2022),
    (2023),
    (2024)
ON CONFLICT (ano) DO NOTHING;

-- Inserção de 5 dados de transformação
INSERT INTO dados_transformacao (atividade_economica_id, componente_id, periodo_id, valor) VALUES
    (1, 1, 1, 10000.50),
    (2, 2, 2, 20000.75),
    (3, 3, 3, 15000.00),
    (4, 4, 4, 18000.25),
    (5, 5, 5, 22000.90);