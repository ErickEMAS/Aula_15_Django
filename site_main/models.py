from django.db import models

# Create your models here.

class Produto(models.model):
    opcoes_tamanho = [('RN', 'rn'),
                      ('PP', 'pp'),
                      ('P', 'p'),
                      ('M', 'm'),
                      ('G', 'g'),
                      ('GG', 'gg'),
                      ('G1', 'g1'),
                      ('G2', 'g2'),
                      ('G3', 'g3'),
                      ('G4', 'g4'),
    ]

    nome = models.CharField(max_length=80)
    preco = models.DecimalField(max_digits=9999, decimal_places=2, default=87)
    disponibilidade = models.BooleanField(default=True)
    quantidade = models.IntegerField(default=1)
    tamanho = models.CharField(max_length=2, choices= opcoes_tamanho)


class Pedido(models.Model):
    metodo_pagamento = [('AV', 'Pagamento à vista'),
                        ('P2', 'Pagamento em 2x'),
                        ('P3', 'Pagamento em 3x'),
    ]

    nome_cliente = models.CharField(max_length=140)
    email = models.EmailField()
    cartao = models.IntegerField()
    pagamento = models.CharField(max_length=2, choices=metodo_pagamento)

