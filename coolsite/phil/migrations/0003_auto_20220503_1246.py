
# Generated by Django 3.0.4 on 2022-05-03 09:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('phil', '0002_quotes'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='books',
            options={'ordering': ['name'], 'verbose_name': 'Прочитанные книги', 'verbose_name_plural': 'Прочитанные книги'},
        ),
        migrations.RenameField(
            model_name='books',
            old_name='description',
            new_name='my_description',
        ),
        migrations.AddField(
            model_name='books',
            name='author_description',
            field=models.TextField(default=1, verbose_name='Описание автора / издательства'),
            preserve_default=False,
        ),
    ]
