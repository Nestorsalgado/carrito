<div class="alert alert-dark" role="alert">
    <table class="table table-bordered">
      <thead>
        <tr>
          <th  colspan="3" class="text-center">CARRITO</th>
        </tr>
        <tr>
          <th scope="col">NOMBRE</th>
          <th scope="col">PRECIO</th>
          <th scope="col">LADRILLOS</th>
        </tr>
      </thead>
      <tbody>
      
      {% if request.session.carrito.items %}
      {% for key, value in request.session.carrito.items %}
        <tr>
          <td>{{value.nombre}}</td>
          <td>{{value.acumulado}}</td>
          <td>{{value.ladrillos}}
            <a href="{% url 'Add' value.propiedad_id %}" class="badge btn btn-dark badge-dark">+</a>
            <a href="{% url 'Sub' value.propiedad_id %}" class="badge btn btn-dark badge-dark">-</a>
          </td>
        </tr>
      {% endfor %}
      {% else %}
      <tr>
          <td colspan="3">
              <div class="alert alert-danger text-center"> SIN LADRILLOS </div>
          </td>
      </tr>
      {% endif %}
      
        <tr>
          <th scope="row">Total:</th>
          <td colspan="2">$ {{total_carrito}}</td>
        </tr>
      </tbody>
    </table>
    <hr>
    </div>
    <div class="row text-center">
        <div class="col-6"><a href="{% url 'Cls' %}" class="btn btn-success">Limpiar</a></div>
        <div class="col-6"><a href="" class="btn btn-info">Guardar</a></div>
    </div>