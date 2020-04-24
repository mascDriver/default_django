# Generated by Django 3.0.2 on 2020-03-01 16:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Brand',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='Nome da Marca')),
                ('active', models.BooleanField(verbose_name='Esta ativo?')),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='Nome da categoria')),
                ('active', models.BooleanField(verbose_name='Esta ativo?')),
            ],
        ),
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='Nome do departamento')),
                ('active', models.BooleanField(verbose_name='Esta ativo?')),
            ],
        ),
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='Nome da imagem')),
                ('image_url', models.ImageField(upload_to='media/', verbose_name='Caminho da imagem')),
                ('active', models.BooleanField(verbose_name='Esta ativo?')),
            ],
        ),
        migrations.CreateModel(
            name='Price',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='Descricao do preco')),
                ('price', models.DecimalField(decimal_places=2, max_digits=15, verbose_name='Valor do preco')),
                ('discount', models.DecimalField(decimal_places=2, max_digits=15, verbose_name='Valor de desconto')),
                ('active', models.BooleanField(verbose_name='Esta ativo?')),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='Nome do produto')),
                ('active', models.BooleanField(verbose_name='Esta ativo?')),
                ('brand', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shop.Brand', verbose_name='Marca do produto')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shop.Category', verbose_name='Categoria do produto')),
                ('department', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shop.Department', verbose_name='Departamento do produto')),
            ],
        ),
        migrations.CreateModel(
            name='Stock',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='Descricao do estoque')),
                ('quantity', models.IntegerField(verbose_name='Quantidade do estoque')),
                ('active', models.BooleanField(verbose_name='Esta ativo?')),
            ],
        ),
        migrations.CreateModel(
            name='Sku',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='Nome do sku')),
                ('width', models.DecimalField(decimal_places=4, max_digits=15, verbose_name='Largura do sku')),
                ('length', models.DecimalField(decimal_places=4, max_digits=15, verbose_name='Comprimento do sku')),
                ('height', models.DecimalField(decimal_places=4, max_digits=15, verbose_name='Altura do sku')),
                ('active', models.BooleanField(verbose_name='Esta ativo?')),
                ('price', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shop.Price', verbose_name='Preco do sku')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shop.Product', verbose_name='Produto Pai')),
                ('stock', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shop.Stock', verbose_name='Quantidade em estoque')),
                ('url_image', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shop.Image', verbose_name='Caminho da imagem do sku')),
            ],
        ),
        migrations.AddField(
            model_name='category',
            name='department',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shop.Department', verbose_name='Departamento da categoria'),
        ),
    ]
