$(document).ready(function(){
	var $followButtons=$(".follow-button")
		,$toggleButton=$(".follow-toggle-button")

		,menuOpen=false
		,buttonsNum=$followButtons.length
		,buttonsMid=(buttonsNum/2)
		,spacing=50
	;

	function openFollowMenu(){
		TweenMax.to($toggleButton,0.1,{
			scaleX:1.2,
			scaleY:0.6,
			ease:Quad.easeOut,
			onComplete:function(){
				TweenMax.to($toggleButton,.8,{
					scale:0.6,
					ease:Elastic.easeOut,
					easeParams:[1.1,0.6]
				})
				TweenMax.to($toggleButton.children(".follow-icon"),.8,{
					scale:1.4,
					ease:Elastic.easeOut,
					easeParams:[1.1,0.6]
				})
			}
		})
		$followButtons.each(function(i){
			var $cur=$(this);
			var pos=i-buttonsMid;
			if(pos>=0) pos+=1;
			var dist=Math.abs(pos);
			$cur.css({
				zIndex:buttonsMid-dist
			});
			TweenMax.to($cur,1.1*(dist),{
				x:pos*spacing,
				scaleY:0.6,
				scaleX:1.1,
				ease:Elastic.easeOut,
				easeParams:[1.01,0.5]
			});
			TweenMax.to($cur,.8,{
				delay:(0.2*(dist))-0.1,
				scale:0.6,
				ease:Elastic.easeOut,
				easeParams:[1.1,0.6]
			})
				
			TweenMax.fromTo($cur.children(".follow-icon"),0.2,{
				scale:0
			},{
				delay:(0.2*dist)-0.1,
				scale:1,
				ease:Quad.easeInOut
			})
		})
	}
	function closeFollowMenu(){
		TweenMax.to([$toggleButton,$toggleButton.children(".follow-icon")],1.4,{
			delay:0.1,
			scale:1,
			ease:Elastic.easeOut,
			easeParams:[1.1,0.3]
		});
		$followButtons.each(function(i){
			var $cur=$(this);
			var pos=i-buttonsMid;
			if(pos>=0) pos+=1;
			var dist=Math.abs(pos);
			$cur.css({
				zIndex:dist
			});

			TweenMax.to($cur,0.4+((buttonsMid-dist)*0.1),{
				x:0,
				scale:.95,
				ease:Quad.easeInOut,
			});
				
			TweenMax.to($cur.children(".follow-icon"),0.2,{
				scale:0,
				ease:Quad.easeIn
			});
		})
	}

	function toggleFollowMenu(){
		menuOpen=!menuOpen

		menuOpen?openFollowMenu():closeFollowMenu();
	}
	$toggleButton.on("mousedown",function(){
		toggleFollowMenu();
	})
	
})