function random_gradient(id = null) {
    let gradients = [
        ["white", "linear-gradient(to top, rgb(55, 236, 186) 0%, rgb(114, 175, 211) 100%)"],
        ["white", "linear-gradient(to top, rgb(68, 129, 235) 0%, rgb(4, 190, 254) 100%)"],
        ['white', "linear-gradient(to top, rgb(199, 144, 129) 0%, rgb(223, 165, 121) 100%)"],
        ['dark', "radial-gradient(at center top, rgba(255, 255, 255, 0.03) 0%, rgba(0, 0, 0, 0.03) 100%), linear-gradient(to top, rgba(255, 255, 255, 0.1) 0%, rgba(143, 152, 157, 0.6) 100%)"],

        ["white", "radial-gradient(248px at center center, rgb(22, 217, 227) 0%, rgb(48, 199, 236) 47%, rgb(70, 174, 247) 100%)"],
        ["white", "linear-gradient(to top, rgb(68, 129, 235) 0%, rgb(4, 190, 254) 100%)"],
        ['white', "linear-gradient(to top, rgb(48, 207, 208) 0%, rgb(51, 8, 103) 100%)"],
        ['white', "linear-gradient(to right, rgb(237, 110, 160) 0%, rgb(236, 140, 105) 100%)"],

    ];
    if (id != null) {
        return gradients[Math.floor(id % gradients.length)];
    } else {
        return gradients[Math.floor(Math.random() * gradients.length)];
    }
}

let coll = document.getElementsByClassName('article');

for (let i = 0, len = coll.length; i < len; i++) {
    let item_image = coll[i].getElementsByClassName('item-image')[0];

    if (item_image !== undefined) {
        if (item_image.style.backgroundImage === "") {
            let gradient = random_gradient(i);
            coll[i].classList.add("text-" + gradient[0]);
            item_image.style.background = gradient[1];
        } else if (item_image.style.backgroundImage !== "") {
            coll[i].classList.add("text-white");
        }
    }
}
