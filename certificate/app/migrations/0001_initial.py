
import app.models

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Attribute',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('color', models.CharField(max_length=16)),
                ('font', models.CharField(max_length=24)),
                ('font_size', models.CharField(max_length=8)),
                ('font_weight', models.CharField(max_length=8)),
            ],
        ),
        migrations.CreateModel(

            name='Body',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=16)),
                ('text', models.TextField(blank=True, null=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to=app.models.upload_to)),
            ],
        ),
        migrations.CreateModel(
            name='Certificate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Component',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('attribute', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.attribute')),
                ('body', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.body')),
            ],
        ),
        migrations.CreateModel(
            name='SizeAndСoordinates',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('x', models.CharField(max_length=8)),
                ('y', models.CharField(max_length=8)),
                ('z', models.CharField(max_length=8)),
                ('width', models.CharField(max_length=8)),
                ('height', models.CharField(max_length=8)),
            ],
        ),
        migrations.CreateModel(

            name='TypeComponent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=16)),

            ],
        ),
        migrations.CreateModel(
            name='Layout',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('certificate', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.certificate')),
                ('component', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.component')),
            ],
        ),
        migrations.AddField(
            model_name='component',
            name='size_and_coordinates',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.sizeandсoordinates'),
        ),
        migrations.AddField(
            model_name='component',
            name='type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.typecomponent'),
        ),
        migrations.AddField(
            model_name='certificate',
            name='component',
            field=models.ManyToManyField(through='app.Layout', to='app.component'),
        ),

    ]
