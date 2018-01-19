/*récuperer tout les marques des voitures disponible*/
$.ajax({
	type : 'GET',
	url : '/annonce/marque/?format=json',
	dataType : "json",
	data : {
		csrfmiddlewaretoken : $('input[name=csrfmiddlewaretoken]').val()
	},
	success : function(response) {

		var availableHints = [];
		for ( var i in response) {
			availableHints.push({
				label : response[i].libelle
			});
		}

		$("#marque").autocomplete({
			source : availableHints,
		});
	}
});

/* récuperer tout les pieces detachées */
$.ajax({
	type : 'GET',
	url : '/annonce/piece/?format=json',
	dataType : "json",
	data : {
		csrfmiddlewaretoken : $('input[name=csrfmiddlewaretoken]').val()
	},
	success : function(response) {

		var availableHints = [];
		for ( var i in response) {
			availableHints.push({
				label : response[i].libelle
			});
		}

		$("#piece").autocomplete({
			source : availableHints,
		});
	}
});
/* *************LISTENER JQUERY************** */
$(function() {
	$.material.init();

	var marque_input;
	var modele_input;
	var piece_input;

	/* récuperer tout les modeles */
	$('#modele').on(
			'focus',
			function() {

				if ($('#marque').val().length == 0) {
					$.ajax({
						type : 'GET',
						url : '/annonce/tout-les-modeles/?format=json',
						dataType : "json",
						data : {
							csrfmiddlewaretoken : $(
									'input[name=csrfmiddlewaretoken]').val()
						},
						success : function(response) {

							var availableHints = [];
							for ( var i in response) {
								availableHints.push({
									label : response[i].libelle
								});
							}

							$("#modele").autocomplete({
								source : availableHints,
							});
						}
					});
				}
			});

	/* récuperer les modeles de la marque selectionner */
	$('#modele').on(
			'focus',
			function() {

				if ($('#marque').val().length > 0) {
					$.ajax({
						type : 'GET',
						url : '/annonce/modele/?format=json',
						dataType : "json",
						data : {
							marque : $('#marque').val(),
							csrfmiddlewaretoken : $(
									'input[name=csrfmiddlewaretoken]').val()
						},
						success : function(response) {

							var availableHints = [];
							for ( var i in response) {
								availableHints.push({
									label : response[i].libelle
								});
							}

							$("#modele").autocomplete({
								source : availableHints,
							});
						}
					});

				}
			});
	/** **********MARQUE CHOISIX********* */
	var marque_clicked;
	var modele_clicked;
	var zone_clicked;
	var piece_clicked;

	$('.img-marque img')
			.on(
					'click',
					function() {
						marque_clicked = $(this).attr('id');
						$.ajax({
							type : 'GET',
							url : '/annonce/modele/?format=json',
							dataType : "json",
							data : {
								marque : marque_clicked,
								csrfmiddlewaretoken : $(
										'input[name=csrfmiddlewaretoken]')
										.val()
							},
							success : function(data) {
								$('.marque-container .btn-fab').removeClass(
										'hidden').addClass('visible');
								$('.img-marque').fadeOut();
								$('.img-modele').fadeIn();
								$('.img-modele').removeClass('hidden')
										.addClass('visible');
							}
						});

						$
								.ajax({
									type : 'GET',
									url : '/annonce/modele-complet//?format=json',
									dataType : "json",
									data : {
										marque : marque_clicked,
										csrfmiddlewaretoken : $(
												'input[name=csrfmiddlewaretoken]')
												.val()
									},
									success : function(data) {

										html = "";
										for (i = 0; i < data.length; i++) {
											html += "<div class='col-md-2 col-sm-3 col-xs-2'><a href='javascript:void(0)'>"
													+ data[i].libelle
													+ "</a></div>"
										}
										$('.img-modele').html(html);
									}
								});

					});
	/* BOUTON RETOURNER VERS LA LISTE DES MARQUES */
	$(".marque-container .btn-fab").on("click", function() {
		$('.img-modele').fadeOut();
		$('.img-zone').fadeOut();
		$('.liste-pieces').fadeOut();
		$('.img-marque').fadeIn(500);

		$(this).addClass('hidden').removeClass('visible');
	});
	/* CLICK SUR UNE ZONE DE VOITURE */
	$('.img-modele').on("click", "a", function() {
		modele_clicked = $(this).text();
		$('.img-modele').fadeOut();
		$('.img-zone').fadeIn();
		$('.img-zone').removeClass('hidden').addClass('visible');
	})
	/* AFFICHER LES PIECE DE LA ZONE */
	$(".img-zone img").on(
			"click",
	function() {
		zone_clicked = $(this).attr('id');

		$.ajax({
			type : 'GET',
			url : '/annonce/zone/?format=json',
			dataType : "json",
			data : {
				zone : $(this).attr('id'),
				csrfmiddlewaretoken : $(
						'input[name=csrfmiddlewaretoken]')
						.val()
			},
			success : function(data) {

				$('.img-zone').fadeOut();
				$('.liste-pieces').fadeIn();
				$('.liste-pieces').removeClass('hidden')
						.addClass('visible');

				html = "";
				for (i = 0; i < data.length; i++) {
					html += "<tr><td class='piece-clicked'>"
						+ data[i].libelle + "</td></tr>";
				}
				$(".liste-pieces table").html(html);
			}
		});
	});
/* filtre table des piéce détaché */
	$('#filter').keyup(function() {

		var rex = new RegExp($(this).val(), 'i');
		$('.searchable tr').hide();
		$('.searchable tr').filter(function() {
			return rex.test($(this).text());
		}).show();

	});

	/***** AFFICHER ANNONCES ****
     *
     * récuperer les annonces liées au modéle et piéce selectionnée
     *
     * */
	$('.table').on('click', 'tr td',function() {
		piece_clicked = $(this).text();

		/*RECUPERER LES ANNONCES DE MARQUE & MODELE & PIECE clicker par image
		*
		*
		*
		* */
			/*Ajax code...*/
	});

	$('#submit').on('click', function(){

		/*RECUPERER LES ANNONCES DE MARQUE & MODELE & PIECE selectionner par filtre input
		*
		* verifier les input vide ou non
		*
		* */
			/*Ajax code...*/
	});
});
