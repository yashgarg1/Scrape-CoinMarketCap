# Create a view that accepts the HTTP POST request and updates the data in the database.
def update_data(request):
    # Get the data from the request.
    data = request.POST.get("data")
    # Create a cryptocurrency object for each piece of data.
    for row in data:
        cryptocurrency = Cryptocurrency(
            name=row["name"],
            price=row["price"],
            one_h_percent=row["1h%"],
            twentyFour_h_percent=row["24h%"],
            seven_d_percent=row["7d%"],
            market_cap=row["market_cap"],
            volume_24h=row["volume(24h)"],
            circulating_supply=row["circulating_supply"],
        )

        # Save the cryptocurrency object in the database.
        cryptocurrency.save()

    return HttpResponse("Data updated successfully.")


def get_latest_data(request):
    # Get the latest cryptocurrency data from the database.
    cryptocurrency_data = Cryptocurrency.objects.all()

    # Return the data as JSON.
    return JsonResponse(cryptocurrency_data.to_json(), safe=False)
