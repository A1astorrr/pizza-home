from django.db import models


# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=150, unique=True, verbose_name="Название")
    slug = models.SlugField(max_length=200, unique=True, blank=True, null=True, verbose_name="URL")
    
    class Meta:
        db_table = 'category'
        verbose_name = "Категори"
        verbose_name_plural = "Категории"
        
    def __str__(self) -> str:
        return self.name

    
class Product(models.Model):
    # удаляя категорию, мы удаляем все ее продукты
    category = models.ForeignKey(to=Category, on_delete=models.CASCADE, verbose_name="Категория")
    name = models.CharField(max_length=150, unique=True, verbose_name="Название")
    slug = models.SlugField(max_length=200, unique=True, blank=True, null=True, verbose_name="URL")
    description = models.TextField(blank=True, null=True, verbose_name="Описание")
    image = models.ImageField(upload_to="goods_images", blank=True, null=True, verbose_name="Изображение")
    price = models.DecimalField(default=0, max_digits=7, decimal_places=0, verbose_name="Цена")
    discount = models.DecimalField(default=0, max_digits=4, decimal_places=0, verbose_name="Скидка в %")
    quantity = models.PositiveIntegerField(default=0, verbose_name="Количество")

    # когда был создан продукт
    created_at = models.DateTimeField(auto_now_add=True)
    
    # показываем новый продукт первым
    class Meta:
        db_table = 'product'
        verbose_name = "Продукт"
        verbose_name_plural = "Продукты"
        
    def __str__(self) -> str:
        return f"{self.name} Количество - {self.quantity}"
    
    # проверка на скидку
    def sell_price(self):
        if self.discount:
            return round(self.price - self.price*self.discount/100)
        
        return self.price
            
        
