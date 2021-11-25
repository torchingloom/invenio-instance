/*
 *   Copyright (C) 2021 RSL.
 *
 * rsl is free software; you can redistribute it and/or modify it under the
 * terms of the MIT License; see LICENSE file for more details.
 */

import $ from "jquery";

$("#files")
  .find(".preview-link")
  .on("click", function(event) {
    $("#preview").show();
    $("#preview-iframe").attr("src", $(event.target).data("url"));
  });
