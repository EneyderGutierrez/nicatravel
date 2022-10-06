# Generated by Django 2.2.19 on 2022-10-04 14:29

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('hotels', '0007_hoteles'),
    ]

    operations = [
        migrations.CreateModel(
            name='hotelesl',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('imageperfil', models.ImageField(upload_to='hotels/images')),
                ('slide', models.ImageField(upload_to='hotels/images')),
                ('slide1', models.ImageField(upload_to='hotels/images')),
                ('slide2', models.ImageField(upload_to='hotels/images')),
                ('namehotel', models.CharField(max_length=30)),
                ('description', models.TextField()),
                ('numeroDeHabitaciones', models.CharField(max_length=30)),
                ('precio', models.CharField(max_length=30)),
                ('desayuno', models.BooleanField(max_length=30)),
                ('ciudad', models.CharField(max_length=30)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.DeleteModel(
            name='hoteles',
        ),
    ]
