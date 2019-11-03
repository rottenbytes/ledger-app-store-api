
from django.db import migrations, models

class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_auto_20190712_1254'),
    ]

    operations = [
        migrations.AddField(
            model_name='applicationversion',
            name='dependency',
            field=models.ForeignKey(
                "application",
                on_delete=models.CASCADE,
                null=True
            ),
        ),
        migrations.AddField(
            model_name='applicationversion',
            name='bytes',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='sefirmwarefinalversion',
            name='blocks',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
